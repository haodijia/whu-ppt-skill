from pathlib import Path
import argparse,json,posixpath,re,zipfile
from lxml import etree as E
N={'p':'http://schemas.openxmlformats.org/presentationml/2006/main','a':'http://schemas.openxmlformats.org/drawingml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
def tag(k):
 p,l=k.split(':');return '{'+N[p]+'}'+l
def create_timing(root,steps):
 timing=E.SubElement(root,tag('p:timing'));counter=iter(range(1,1000))
 def ctn(parent,**attrs):return E.SubElement(parent,tag('p:cTn'),{'id':str(next(counter)),**attrs})
 def cond(ct,delay):E.SubElement(E.SubElement(ct,tag('p:stCondLst')),tag('p:cond'),{'delay':delay})
 lst=E.SubElement(timing,tag('p:tnLst'));rt=ctn(E.SubElement(lst,tag('p:par')),dur='indefinite',restart='never',nodeType='tmRoot');seq=E.SubElement(E.SubElement(rt,tag('p:childTnLst')),tag('p:seq'),{'concurrent':'1','nextAc':'seek'});main=ctn(seq,dur='indefinite',nodeType='mainSeq');mainlist=E.SubElement(main,tag('p:childTnLst'))
 builds=[]
 for step in steps:
  outer=ctn(E.SubElement(mainlist,tag('p:par')),fill='hold');cond(outer,'indefinite');inner=ctn(E.SubElement(E.SubElement(outer,tag('p:childTnLst')),tag('p:par')),fill='hold');cond(inner,'0');effects=E.SubElement(inner,tag('p:childTnLst'))
  for j,(sid,visible) in enumerate(step):
   effect=ctn(E.SubElement(effects,tag('p:par')),presetID='1',presetClass='entr' if visible else 'exit',presetSubtype='0',fill='hold',grpId='0' if visible else '1',nodeType='clickEffect' if j==0 else 'withEffect');cond(effect,'0')
   st=E.SubElement(E.SubElement(effect,tag('p:childTnLst')),tag('p:set'));bh=E.SubElement(st,tag('p:cBhvr'));ct=ctn(bh,dur='1',fill='hold');cond(ct,'0');E.SubElement(E.SubElement(bh,tag('p:tgtEl')),tag('p:spTgt'),{'spid':sid});E.SubElement(E.SubElement(bh,tag('p:attrNameLst')),tag('p:attrName')).text='style.visibility';E.SubElement(E.SubElement(st,tag('p:to')),tag('p:strVal'),{'val':'visible' if visible else 'hidden'});builds.append((sid,'0' if visible else '1'))
 for prefix,evt in [('prev','onPrev'),('next','onNext')]:
  co=E.SubElement(E.SubElement(seq,tag('p:'+prefix+'CondLst')),tag('p:cond'),{'evt':evt,'delay':'0'});E.SubElement(E.SubElement(co,tag('p:tgtEl')),tag('p:sldTgt'))
 bl=E.SubElement(timing,tag('p:bldLst'))
 for sid,grp in dict.fromkeys(builds):E.SubElement(bl,tag('p:bldP'),{'spid':sid,'grpId':grp,'uiExpand':'1','animBg':'1'})

def main():
 parser=argparse.ArgumentParser(description='Bind named WHU method shapes to native click animations.')
 parser.add_argument('--input',type=Path,required=True)
 parser.add_argument('--output',type=Path,required=True)
 parser.add_argument('--slide',type=int,required=True)
 args=parser.parse_args()
 if args.input.resolve()==args.output.resolve():parser.error('Input and output must differ.')
 if args.output.exists():parser.error('Output already exists.')
 with zipfile.ZipFile(args.input) as z:parts={n:z.read(n) for n in z.namelist()}
 pres=E.fromstring(parts['ppt/presentation.xml']);slides=pres.findall('p:sldIdLst/p:sldId',N)
 if args.slide<1 or args.slide>len(slides):parser.error('Slide is out of range.')
 rid=slides[args.slide-1].get('{'+N['r']+'}id')
 rel=next(r for r in E.fromstring(parts['ppt/_rels/presentation.xml.rels']) if r.get('Id')==rid)
 part=posixpath.normpath(posixpath.join('ppt',rel.get('Target')))
 root=E.fromstring(parts[part]);ids={}
 for obj in root.findall('.//p:cNvPr',N):
  name=obj.get('name','')
  if re.fullmatch(r'(HIGHLIGHT|EXPLAIN)_\d+',name):
   if name in ids:parser.error('Duplicate object name: '+name)
   ids[name]=obj.get('id')
 numbers=sorted(int(n.split('_')[1]) for n in ids if n.startswith('HIGHLIGHT_'))
 if not numbers or numbers!=list(range(1,len(numbers)+1)):parser.error('Highlight numbers must be consecutive from 1.')
 if set(ids)!={f'{prefix}_{i}' for prefix in ['HIGHLIGHT','EXPLAIN'] for i in numbers}:parser.error('Every highlight requires exactly one paired explanation.')
 for old in list(root):
  if old.tag==tag('p:timing'):root.remove(old)
 steps=[]
 for i in numbers:
  actions=[(ids[f'EXPLAIN_{i}'],True)]
  if i>1:actions.append((ids[f'HIGHLIGHT_{i-1}'],False))
  actions.append((ids[f'HIGHLIGHT_{i}'],True));steps.append(actions)
 create_timing(root,steps)
 # In CT_Slide, timing precedes extLst.
 timing=root.find('p:timing',N);ext=root.find('p:extLst',N)
 if ext is not None:root.remove(timing);root.insert(list(root).index(ext),timing)
 known={x.get('id') for x in root.findall('.//p:cNvPr',N)}
 if any(x.get('spid') not in known for x in timing.findall('.//p:spTgt',N)):raise RuntimeError('Missing animation target.')
 parts[part]=E.tostring(root,encoding='utf-8',xml_declaration=True)
 args.output.parent.mkdir(parents=True,exist_ok=True)
 with args.output.open('xb') as stream:
  with zipfile.ZipFile(stream,'w',zipfile.ZIP_DEFLATED) as z:
   for name,data in parts.items():z.writestr(name,data)
 print(json.dumps({'output':str(args.output),'slide':args.slide,'click_steps':len(steps),'behavior':'accumulate explanations and replace highlight'}))
if __name__=='__main__':main()
