function saveToDo(e){
    e.preventDefault()
    let desc = document.getElementById("task_desc").value
    let title = document.getElementById("task_title").value

    if(desc.length<5 || title.length<5){
        alert("Veuillez completez les champs requis")
        return
    }

    fetch("/save_to_do/",{
        method: "POST",
        body: JSON.stringify({
                'title' : title,
                'description':desc
            }
        ),
        headers: {
          'Content-Type': 'application/json',
        }
    })
    .then(response => response.json())
    .then(jsonResponse => {
        alert(`La tache ${jsonResponse.title} a ete enregistre avec success`)
        window.location.assign("/")
    })
    .catch(function(){
        alert("Une erreur s'est produite lors de l'enregistrement")
    })
}

document.getElementById("formSave").addEventListener("submit",saveToDo)

function deleteItem(itemID){
    fetch(`/delete_task/${itemID}`).then(resp=>resp.json())
    .then(jsonResponse=>{
        if(jsonResponse.status=="ok"){
            alert(`La tache a ete supprime avec success`)
            window.location.assign("/")
        }
        else
            throw "error"
    })
    .catch(function(){
        alert("Une erreur s'est produite lors de la suppression")
    })
}