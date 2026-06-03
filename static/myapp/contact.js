    const bro = document.getElementById("contactForm");
    

    bro.addEventListener("submit", async function func (e) {

        e.preventDefault();

        const data = {
            name: bro.name.value,
            secondName: bro.secondName.value,
            email: bro.email.value,
            phoneNumber: bro.phoneNumber.value,
            notes: bro.notes.value
        };

        console.log(data);

        try {

            const response = await fetch("/contacts/", {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(data)
            });

            const result = await response.json();

            console.log(result);
            window.location.reload();

        } catch (error) {

            console.error(error);

        }

    });

    
