"use strict";
/*    JavaScript 7th Edition
      Chapter 5
      Chapter Case

      Application to generate a slide show
      Author: Jonathan Au - 300827701
      Date:   2023/03/03

      Filename: js05.js
*/



window.addEventListener("load", setupGallery);

function setupGallery() {
   let imageCount = imgFiles.length;
   let galleryBox = document.getElementById("lightbox");
   let currentSlide = 1;
   let runShow = true;
   let showRunning;
   
   let galleryTitle = document.createElement("h1");
   galleryTitle.id = "galleryTitle";
   let slidesTitle = lightboxTitle; // TODO figure out title
   galleryTitle.textContent = slidesTitle;
   galleryBox.appendChild(galleryTitle);
   
   let slideCounter = document.createElement("div");
   slideCounter.id = "slideCounter";
   slideCounter.textContent = currentSlide + "/" + imageCount;
   galleryBox.appendChild(slideCounter);
   
   let leftBox = document.createElement("div");
   leftBox.id = "leftBox";
   leftBox.innerHTML = "&#9664;";
   leftBox.onclick = moveToLeft;   
   galleryBox.appendChild(leftBox);
   
   let rightBox = document.createElement("div");
   rightBox.id = "rightBox";
   rightBox.innerHTML = "&#9654;";  
   rightBox.onclick = moveToRight;   
   galleryBox.appendChild(rightBox);
   
   let playPause = document.createElement("div");
   playPause.id = "playPause";
   playPause.innerHTML = "&#9199;";
   playPause.onclick = startStopShow;
   galleryBox.appendChild(playPause);
   
   let slideBox = document.createElement("div");
   slideBox.id = "slideBox";
   galleryBox.appendChild(slideBox);
   
   
   for (let i = 0; i < imageCount; i++) {
      let image = document.createElement("img");
      image.src = imgFiles[i];
      image.alt = imgCaptions[i];
      image.onclick = createModal;
      slideBox.appendChild(image);
   }
   
   
   function moveToRight() {
      let firstImage = slideBox.firstElementChild.cloneNode("true");
      firstImage.onclick = createModal;
      slideBox.appendChild(firstImage);
      slideBox.removeChild(slideBox.firstElementChild);
      currentSlide++;
      if (currentSlide > imageCount) {
         currentSlide = 1;
      }
      slideCounter.textContent = currentSlide + " / " + imageCount;
   }
   
   function moveToLeft() {
      let lastImage = slideBox.lastElementChild.cloneNode("true");
      lastImage.onclick = createModal;
      slideBox.removeChild(slideBox.lastElementChild);
      slideBox.insertBefore(lastImage, slideBox.firstElementChild);
      currentSlide--;
      if (currentSlide === 0) {
         currentSlide = imageCount;
      }
      slideCounter.textContent = currentSlide + " / " + imageCount;      
   }  
   
   function startStopShow() {
      if (runShow) {
         showRunning = window.setInterval(moveToRight, 2000);
         runShow = false;
      } else {
         window.clearInterval(showRunning);
         runShow = true;
      }
   }
   
   //Favourites Section
   let favouritesSection = document.getElementById("favourites");
   let favTitle = document.createElement("h2");
   favTitle.id = "favTitle";
   favTitle.textContent = "My Favourites";
   favouritesSection.appendChild(favTitle);
   
   //Favourites Section basic
   let favSection = document.createElement("div");
   favSection.id = "favSection";
   favouritesSection.appendChild(favSection);

   function createModal() {
      let modalWindow = document.createElement("div");
      modalWindow.id = "lbOverlay";
      let figureBox = document.createElement("figure");
      modalWindow.appendChild(figureBox);
      
      let modalImage = this.cloneNode("true");
      figureBox.appendChild(modalImage);
      
      let figureCaption = document.createElement("figcaption");
      figureCaption.textContent = modalImage.alt;
      figureBox.appendChild(figureCaption);
      
      let closeBox = document.createElement("div");
      closeBox.id = "lbOverlayClose";
      closeBox.innerHTML = "&times;";
      closeBox.onclick = function() {
         document.body.removeChild(modalWindow);
      }


      //Image Clone
      let cloneImg = this.cloneNode("true");
      cloneImg.id = "favClone";
      
      
      //button link
      let favButton = document.createElement("div");
      favButton.id = "faveButton";
      favButton.innerHTML = "To Favourites";

      //Image Clone Remove link
      let removeButton = document.createElement("div");
      removeButton.id = "removeButton";
      removeButton.textContent = "Remove";
      
      
      //Fav Image Exists
      //let favExists =false;
      let clickCounter = false;

      favButton.onclick = function favBut() {
         //Image Click link
         let imgClick = document.createElement("favImg");
         //imgClick.id = "imgClick";
         
         //clone image to favourites
         if (favCount >= favLimit) {
            window.alert("Error: you have exceeded the limit (5)");
         }else if (favSection.contains(cloneImg)) {
            //if the image already exists in the list
            //run this error
            window.alert("This Image is already in your Favourites.");
         }else if (favCount < 0) {
            window.alert("Error: How on earth did you trigger this?");
         }else {
            cloneImg.appendChild(imgClick)
            favCount++;
            function clonePict(){
               favSection.appendChild(cloneImg);
               cloneImg.appendChild(removeButton);
               favSection.insertBefore(removeButton, cloneImg);
            }
            clonePict();
            removeButton.setAttribute("hidden","");
            console.log("Adding to Favourites...")
            console.log(favCount);
            //favExists = true;
         }
      } 
      
      cloneImg.onclick = function rmClone() {
         if (clickCounter == false) {
            //create remove button
            console.log("creating remove button...");
            removeButton.removeAttribute('hidden');
            console.log(clickCounter);
            clickCounter = true;
         } else {
            console.log("Deleting remove button...");
            removeButton.setAttribute("hidden","");
            console.log(clickCounter);
            clickCounter = false;
         }
      }

      //Remove clone
      removeButton.onclick = function rmBut() {
         favCount --;
         cloneImg.remove();
         removeButton.remove();
         console.log("Removing from Favourites...");
         console.log(favCount);
         //favExists = false;
      }
      
      modalWindow.appendChild(closeBox);
      modalWindow.appendChild(favButton);
      
      document.body.appendChild(modalWindow);
   }

   //Image Counter
   let favCount = 0;
   let favLimit = 5;

}