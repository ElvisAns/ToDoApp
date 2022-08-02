function saveToDo(e){
    e.preventDefault()
    let desc = document.getElementById("task_desc").value
    let title = document.getElementById("task_title").value

    if(desc.length<5 || title.length<5){
        alert("Veuillez completez les champs requis")
        return
    }

    fetch("/todo/save_to_do/",{
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
        const tr = document.createElement("tr")
        tr.setAttribute("id",`itemno${ jsonResponse.id }`)
        tr.innerHTML = `
        <td>${jsonResponse.id}</td>
        <td><h6 class="text-primary">${ jsonResponse.title }</h6><p>${jsonResponse.description}</p></td>
        <td>
            <span class="text-danger">No</span>
        </td>
        <td>${ jsonResponse.date }</td>
        <td>
            <div class="row row-cols-lg-auto justify-content-center align-items-start">
                <button onclick="deleteItem('${jsonResponse.id }')" type="submit" class="btn btn-danger m-1">Delete</button>
                <button onclick="makeAsDone('${ jsonResponse.id }')" type="submit" class="btn btn-success m-1">Finished</button>
            </div>
        </td>
        `;
        document.getElementById("todos").appendChild(tr)

        alert(`La tache ${jsonResponse.title} a ete enregistre avec success`)
        //window.location.assign("/")
    })
    .catch(function(){
        alert("Une erreur s'est produite lors de l'enregistrement")
    })
}

document.getElementById("formSave").addEventListener("submit",saveToDo)

function deleteItem(itemID){
    fetch(`/todo/delete_task/${itemID}`).then(resp=>resp.json())
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

function makeAsDone(itemID){
    fetch(`/todo/make_complete/${itemID}`).then(resp=>resp.json())
    .then(jsonResponse=>{
        if(jsonResponse.status=="ok"){
            alert(`La tache a ete marqued complete avec success`)
            window.location.assign("/")
        }
        else
            throw "error"
    })
    .catch(function(){
        alert("Une erreur s'est produite lors de la mis a jour de la tache")
    })
}