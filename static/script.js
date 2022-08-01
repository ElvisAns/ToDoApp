function saveToDo(e){
    e.preventDefault()
    let desc = document.getElementsById("task_desc").value
    let title = document.getElementById("task_title").value

    if(desc.length<5 || title.length<5){
        alert("Veuillez completez les champs requis")
        return
    }

    fetch("/save_to_do/",{
        method:POST,
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
    })
    .catch(function(){
        alert("Une erreur s'est produite lors de l'enregistrement")
    })
}

document.getElementById("formSave").addEventListener("submit",saveToDo)