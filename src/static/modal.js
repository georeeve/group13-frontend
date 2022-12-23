[...document.getElementsByClassName("modal")].forEach(element => {
    const modal = new bootstrap.Modal(element);
    modal.show();
});
