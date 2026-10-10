"""Public GET-only check. No API key, code upload, paid call or invoice."""
import json,os
from urllib.request import Request,build_opener,HTTPRedirectHandler
class NoRedirect(HTTPRedirectHandler):
 def redirect_request(self,*args,**kwargs):raise ValueError('Redirect refused')
def fetch(path):
 if path not in ('models','payments/terms'):raise ValueError('Unsupported route')
 with build_opener(NoRedirect()).open(Request('https://1nfer.net/v1/'+path,headers={'User-Agent':'1NFER public CI connectivity check'}),timeout=20) as r:
  raw=r.read(262145)
  if len(raw)>262144:raise ValueError('Response too large')
  data=json.loads(raw)
  if not isinstance(data,dict):raise ValueError('Invalid response')
  return data

def check(get=fetch):
 rows=get('models').get('data');terms=get('payments/terms')
 if not isinstance(rows,list) or not rows or not all(isinstance(x,dict) and isinstance(x.get('id'),str) for x in rows):raise ValueError('No valid advertised models')
 if type(terms.get('enabled'))!=bool:raise ValueError('Invalid payment status')
 return {'model-count':str(len(rows)),'funding-enabled':str(terms['enabled']).lower()}
def main():
 try:result=check()
 except Exception:print('1NFER public connectivity check failed; no paid call or automatic retry.');return 1
 if os.environ.get('GITHUB_OUTPUT'):
  with open(os.environ['GITHUB_OUTPUT'],'a') as f:
   for k,v in result.items():f.write(k+'='+v+'\n')
 if os.environ.get('GITHUB_STEP_SUMMARY'):
  with open(os.environ['GITHUB_STEP_SUMMARY'],'a') as f:f.write('## 1NFER connection check\nAdvertised models: '+result['model-count']+'. New crypto invoices enabled: '+result['funding-enabled']+'.\n\nGET-only, no key/signup/paid generation. Catalogue availability does not prove model completions or quality.\n\n[Inspectable integration guide](https://1nfer.net/guides/crypto-inference-agents.html?utm_source=github_action&utm_medium=ci&utm_campaign=connection_check) · [Scoped router setup](https://hesoyam.business/router)\n')
 print(json.dumps(result));return 0
if __name__=='__main__':raise SystemExit(main())
