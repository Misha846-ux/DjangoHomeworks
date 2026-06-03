const deleteform = document.getElementById("deleteForm");

deleteform.addEventListener("submit", async function func2 (e) {
        e.preventDefault();
        console.log(deleteform.id.value);
        id = Number(deleteform.id.value);
        console.log(id);


        await fetch(`/home/${id}`, {
        method: "DELETE",
        })
        document.location.reload();
    });