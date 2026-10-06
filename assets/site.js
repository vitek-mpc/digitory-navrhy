
const menuBtn=document.querySelector('.menu-btn');
menuBtn?.addEventListener('click',()=>{document.body.classList.toggle('menu-open');menuBtn.setAttribute('aria-expanded',String(document.body.classList.contains('menu-open')))});
document.querySelectorAll('.nav a').forEach(a=>a.addEventListener('click',()=>document.body.classList.remove('menu-open')));
const form=document.querySelector('.form');
form?.addEventListener('submit',e=>{e.preventDefault();const data=new FormData(form);const name=data.get('name')||'';const phone=data.get('phone')||'';const note=data.get('note')||'';const recipient=form.dataset.email;const subject=encodeURIComponent('Poptávka z webu');const body=encodeURIComponent('Jméno: '+name+'\nTelefon: '+phone+'\n\nPoptávka:\n'+note);document.querySelector('.form-status').textContent='Otevírám e-mailovou aplikaci s připravenou poptávkou.';window.location.href='mailto:'+recipient+'?subject='+subject+'&body='+body});
