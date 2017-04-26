$(document).ready(function(){

$( "p" )
  .mouseenter(function() {
    $(this).toggleClass("mouseOver");
  })
  .mouseleave(function() {
    $(this).toggleClass("mouseOver");
  });

$( "#changeBackground" )
  .mouseenter(function() {
    $(this).toggleClass("changeBackground");
  })
  .mouseleave(function() {
    $(this).toggleClass("changeBackground");
  });

  $( "#logo" )
  .mouseenter(function() {
    $(this).toggleClass("rotate");
  })
  .mouseleave(function() {
    $(this).toggleClass("rotate");
  });

   $( "#logo" )
  .click(function() {
    window.location = 'file:///Users/Leibel/Desktop/dojo_assignments/WebFundamentals/Javascript/jQuery/JqueryFunctionsProject/jQueryFunctions.html';
  });

  $( "#whyRun" )
  .click(function() {
    window.location = 'http://www.runnersworld.com/start-running/6-ways-running-improves-your-health';
  });

  $( ".cashApp" )
  .click(function() {
    window.location = 'https://cash.me/$leibelh';
  });

  $("input").keypress(function(e) {
    if(e.which == 13) {
        window.location = 'https://cash.me/$leibelh';
    }
});
 
//   $( "#changeBackground" )
//   .click(function() {
//     $("#container").css("rotate");
//   })
//   .mouseleave(function() {
//     $(this).toggleClass("rotate");
//   });
  
  

 var images = ['http://www.runsfm.com/wp-content/uploads/2016/02/The-Importance-of-Sleep-Before-a-Marathon-2.jpg', 'http://www.runnersworld.com/sites/runnersworld.com/files/styles/slideshow-desktop/public/houston_550.jpg?itok=OL8jTefN', 'https://www.sdcb.org/images/Marathon.jpg', 'http://d279m997dpfwgl.cloudfront.net/wp/2016/04/runners.jpg'];
 
 $('#container').css({'background-image': 'url(' + images[Math.floor(Math.random() * images.length)] + ')'});


$( "#changeBackground" )
  .click(function() {
    $('#container').css({'background-image': 'url(' + images[Math.floor(Math.random() * images.length)] + ')'});
  });





 


});

