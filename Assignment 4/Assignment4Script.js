/*
      Author: J.Au - 300827701
      Date:   2023/04/14

      Filename: Assignment4.html
*/

let ib = 0;


window.addEventListener("load", ()=> {
    var newhttp = new XMLHttpRequest();

    function openModal(y) {
        let modalWindow = document.createElement("div");
        modalWindow.id = "lbOverlay";
        let figureBox = document.createElement("figure");
        modalWindow.appendChild(figureBox);
        
        let modalImage = document.createElement('img');
        modalImage.src = y.src;
        figureBox.appendChild(modalImage);
        
        let alt = document.createElement("figcaption");
        alt.textContent = y.alt;
        figureBox.appendChild(alt);

        let price = document.createElement("figcaption");
        price.textContent = y.price;
        figureBox.appendChild(price);

        let description = document.createElement("figcaption");
        description.textContent = y.description;
        figureBox.appendChild(description);

        
        let closeBox = document.createElement("div");
        closeBox.id = "lbOverlayClose";
        closeBox.innerHTML = "&times;";
        closeBox.onclick = function() {
           document.body.removeChild(modalWindow);
        }

        modalWindow.appendChild(closeBox);
        document.body.appendChild(modalWindow);
    }
    
    if (ib == 0) {
        ib = 1;
        var elem = document.getElementById("myBar");
        var width = 10;
        var id = setInterval(frame, 1000);
        function frame() {
            if (width >= 100) {
                clearInterval(id);
                ib = 0;
            } else {
                width = width + 10;
                elem.style.width = width + "%";
            }
        }
    }
    
    function displayMyImages(responseData) {
        const newArray = JSON.parse(responseData);
        newContainer = document.getElementById('container');

        
        setTimeout( function(){
            for (let i = 0; i < newArray.length; i++) {
                console.log('display images', newArray[i].src);
                console.log('display title', newArray[i].title);
                console.log('display price', newArray[i].price);
                console.log('display description', newArray[i].description);
                console.log('display actionLabel', newArray[i].actionLabel);
                
                var newCol = document.createElement('div');
                newCol.id = "collumn";
    
                var newImg = document.createElement('img');
                newImg.src = newArray[i].src;
    
                var newTitle = document.createElement('p');
                newTitle.innerHTML = newArray[i].title;
    
                var newPrice = document.createElement('p');
                newPrice.innerHTML = newArray[i].price;
                newPrice.id = "price";
    
                var newDescription = document.createElement('p');
                newDescription.innerHTML = newArray[i].description;
    
                var newActionLabel = document.createElement('button');
                newActionLabel.innerHTML = newArray[i].actionLabel;
                
                newActionLabel.addEventListener("click", ()=> {
                    fetch(newArray[i].actionURL)
                    .then(x => x.json())
                    .then(y => openModal(y));
                });
                newContainer.appendChild(newCol);
                newCol.appendChild(newImg);
                newCol.appendChild(newTitle);
                newCol.appendChild(newPrice);
                newCol.appendChild(newDescription);
                if (newArray[i].actionLabel !== undefined) {
                    newCol.appendChild(newActionLabel);
                };    
            };
        }, 9000);
        
        
    };
    
    newhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            displayMyImages(newhttp.responseText);
            //console.log('newhttp', newhttp.responseText);
        };
    };
    newhttp.open("GET", "products.json", true);
    newhttp.send();
});

toggleState = 0;
function toggle() {
    var element = document.body;
    element.classList.toggle("dark-mode");
    let darkBtn = document.getElementById("darkMode");
    if (toggleState == 0) {
        darkBtn.innerHTML = "Let there be light!";
        toggleState = 1;
        console.log(to);
    } else if (toggleState == 1) {
        darkBtn.innerHTML = "Too Bright!";
        toggleState = 0;
    };
};