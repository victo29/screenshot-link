export async function sendLink(link) {
    
    
    try{
        const response = await fetch("http://127.0.0.1:5000/download",{
            method:'POST',
            headers:{
                'Content-Type':'application/json',
            },
            body:JSON.stringify({link: link})

        });
        return await response.json();
    } catch(error){
        throw new Error();
    }
    

}