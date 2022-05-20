var pages = document.getElementsByClassName("page");

function getTimeout(ms) {

    return new Promise(resolve => setTimeout(resolve, ms));

}

async function demo() {

    await getTimeout(1040);
    pages[1].innerText = "";
    await getTimeout(240)
    pages[2].innerText = "";
    await getTimeout(420);
    pages[3].innerText = "";

}

demo();

