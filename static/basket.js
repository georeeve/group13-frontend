[...document.getElementsByClassName("update-item")].forEach((form) => {
    form.addEventListener("submit", (e) => updateBasket(form, e));
});

[...document.getElementsByClassName("delete-item")].forEach((form) => {
    form.addEventListener("submit", (e) => deleteItem(form, e));
})

async function updateBasket(form, e) {
    e.preventDefault();
    const formData = new FormData(form);

    const itemId = form.id.split("item-")[1];
    const quantity = formData.get("quantity");
    await fetch("/basket/update", {
        method: "POST",
        body: JSON.stringify({ itemId, quantity }),
        headers: { "Content-Type": "application/json" },
    });
}

async function deleteItem(form, e) {
    e.preventDefault();

    const itemId = form.id.split("item-")[1];
    await fetch("/basket/delete", {
        method: "POST",
        body: JSON.stringify({ itemId }),
        headers: { "Content-Type": "application/json" }
    });
    location.reload();
}
