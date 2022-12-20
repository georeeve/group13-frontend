[...document.getElementsByClassName("add-item")].forEach(form => {
    form.addEventListener("submit", (e) => addToBasket(form, e));
});

function addToBasket(form, e) {
    e.preventDefault();
    const formData = new FormData(form);

    const itemId = form.id.split("item-")[1];
    const quantity = formData.get("quantity");
    fetch("/basketadd", { method: "POST", body: JSON.stringify({ itemId, quantity }), headers: { "Content-Type": "application/json" } })
}
