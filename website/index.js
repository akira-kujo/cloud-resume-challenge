const counter = document.querySelector(".counter-number"); //store visual counter as var
async function updateCounter() {
    let response = await fetch("https://i3xclbc2k7aamfuyneuc2gi7f40ikeum.lambda-url.eu-west-1.on.aws/"); //request visitor count from api 
    let data = await response.json(); //store response data into variable data
    counter.innerHTML = `Views: ${data}`; //store data into views element on webpage
}

updateCounter(); //call function