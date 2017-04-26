$(document).ready(function(){

    // $( "select" )
    //     .change(function () {
    //         var str = "";
    //         $( "select option:selected" ).each(function() {
    //             $(this).attr('src', 'raphael.png');
    //         });

    $('select').on('change', function() {
        var value = $(this)[0].value;
            if ($(this)[0].name === "Player 1") {
                
                $("#player1Img").attr("src", value +".png");
            } else {
                $("#player2Img").attr("src", value +".png");
            }
            console.log($(this)[0].name);
            console.log($(this)[0].value);
        });
            
   
    $( "button" )
        .click(function() {
            var text = $(this).text();
            console.log(text);
             $("#wrapper").css("background-image", "url('" + text + ".jpg')");
             $("#header").hide();
    });
    // $( "#planet" )
    //     .click(function() {
    //          $("#wrapper").css("background-image", "url('planet.jpg')");
    //          $("#header").hide();
    // });$( "#dojo" )
    //     .click(function() {
    //          $("#wrapper").css("background-image", "url('dojo.jpg')");
    //          $("#header").hide();
    // });$( "#forest" )
    //     .click(function() {
    //          $("#wrapper").css("background-image", "url('forest.jpg')");
    //          $("#header").hide();
    // });$( "#matrix" )
    //     .click(function() {
    //          $("#wrapper").css("background-image", "url('matrix.jpg')");
    //          $("#header").hide();
    // });$( "#snow" )
    //     .click(function() {
    //          $("#wrapper").css("background-image", "url('snow.jpg')");
    //          $("#header").hide();
    // });

    


});