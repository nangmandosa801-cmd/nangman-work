const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:740,height:900}});
await p.setContent('<html><body style="margin:0;padding:20px;width:693px;font-family:sans-serif">'+require('fs').readFileSync('post.html','utf8')+'</body></html>');
await p.screenshot({path:'shot.png',fullPage:true});await b.close()})();
