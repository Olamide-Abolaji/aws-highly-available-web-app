async function loadServerInfo(){
  const fallback={instance_id:"local-demo",availability_zone:"local",private_ip:"127.0.0.1"};
  try{
    const r=await fetch("/api/server-info",{cache:"no-store"});
    if(!r.ok) throw new Error();
    const d=await r.json();
    document.querySelector("#instance").textContent=d.instance_id||fallback.instance_id;
    document.querySelector("#az").textContent=d.availability_zone||fallback.availability_zone;
    document.querySelector("#ip").textContent=d.private_ip||fallback.private_ip;
  }catch(e){
    document.querySelector("#instance").textContent=fallback.instance_id;
    document.querySelector("#az").textContent=fallback.availability_zone;
    document.querySelector("#ip").textContent=fallback.private_ip;
  }
}
loadServerInfo();
