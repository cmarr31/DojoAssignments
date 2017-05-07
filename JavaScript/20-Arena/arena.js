$(document).ready(function(){
    $('select').on('change', function() {
        var value = $(this)[0].value;
        if ($(this)[0].name === "Player 1") {
            $("#player1").attr("src", value +".png");
        } else if ($(this)[0].name === "Player 2") {
            $("#player2").attr("src", value +".png");
        }
    });  
    $( "button" ).click(function() {
        $("#header").hide();
    });
    $( "button" ).hover(function() {
        var text = $(this).text();
        $("#wrapper").css("background-image", "url('" + text + ".jpg')");
    });
});