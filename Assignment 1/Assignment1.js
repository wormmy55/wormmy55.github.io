function toggle() {
    var element = document.body;
    element.classList.toggle("dark-mode");
}

window.addEventListener("load", (event) => {
    console.log("page has been loaded...");
    multiTable()
})

multiTable = () => {
    const element = document.getElementById("myTable");
    const tableElem = document.createElement("table");
    const trElem = document.getElementById("tableList");
    tableElem.setAttribute("id", "tableList")
    element.appendChild(tableElem);
    var rowLimit = 10;
    var colLimit = 10;
    x = 1;
    y = 1;

    if (trElem) {
        trElem.remove();
    }


    if (rowMax.value && colMax.value) {
        rowLimit = rowMax.value;
        colLimit = colMax.value;
    }
    

    for (let rowCounter = 0; rowCounter < rowLimit; rowCounter ++) {
        //Rows
        const rowtr = document.createElement("tr");
        tableElem.appendChild(rowtr);

        for (let colCounter = 0; colCounter < colLimit; colCounter ++){
            z = x * y;
            console.log(rowCounter, colCounter);
            const colItem = document.createElement("td");
            const colnode = document.createTextNode(+x+ ' x '+y+ ' = ' +z+ '');
            colItem.appendChild(colnode);
            rowtr.appendChild(colItem);
            y = y + 1;
        }
        y = 1;
        x = x + 1;
    }
}
