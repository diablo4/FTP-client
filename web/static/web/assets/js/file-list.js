let fileList = document.getElementsByClassName('file-list');

let currentPath = document.getElementById('current-path').innerText;

console.log(currentPath);

for(let i = 0; i < fileList.length; i++) {

    if(fileList[i].innerText.split("")[0] === "d") {
        let x = document.createElement("A");
        let v = document.createTextNode(fileList[i].innerText.split(" ").pop());
        x.appendChild(v);
        let path = currentPath +'/' + fileList[i].innerText.split(" ").pop();

        x.setAttribute("href", "http://localhost:8000/path?path=" + path);

        fileList[i].appendChild(x);

        console.log(fileList[i].innerText)
    } else {
        let x = document.createElement("A");
        let v = document.createTextNode(fileList[i].innerText.split(" ").pop());

        let path = currentPath +'/' + fileList[i].innerText.split(" ").pop();

        x.appendChild(v);
        x.setAttribute("href", "http://localhost:8000/download?path=" + path);

        fileList[i].appendChild(x);

        console.log(fileList[i].innerText)
    }
}

let getList = (data) => {
    // data "[a, b, c]";

    data.trim()
}
