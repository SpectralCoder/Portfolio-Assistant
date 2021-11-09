         const txts=document.querySelector(".animate-text").children,
               txtsLen=txts.length;
           let index=0;
          const textInTimer=3000,
                textOutTimer=2800;

         function animateText() {
            for(let i=0; i<txtsLen; i++){
              txts[i].classList.remove("text-in","text-out");  
            }
            txts[index].classList.add("text-in");

            setTimeout(function(){
                txts[index].classList.add("text-out");              
            },textOutTimer)

            setTimeout(function(){

              if(index == txtsLen-1){
                  index=0;
                }
               else{
                   index++;
                 }
                animateText();
            },textInTimer); 
         }
         
         window.onload=animateText;
   
   //========================
//NAVBAR
//========================
(function ($) {
    $(document).ready(function () {

        // hide .navbar first
        $(".pernavbar").hide();

        // fade in .navbar
        $(function () {
            $(window).scroll(function () {

                // set distance user needs to scroll before we start fadeIn
                if ($(this).scrollTop() > 90) {
                    $('.pernavbar')
                        .removeClass('animated fadeOutUp')
                        .addClass('animated fadeInDown')
                        .fadeIn();

                } else {
                    $('.pernavbar')
                        .removeClass('animated fadeInDown')
                        .addClass('animated fadeOutUp')
                        .fadeOut();
                }
            });
        });

    });
}(jQuery));