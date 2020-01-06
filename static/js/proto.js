$("document").ready(function() {
  $("#toggler2").click(function() {
    $("#left-form").hide();
    $("#right-list").css("grid-column","1/3");
  });

  $("#toggler1").click(function() {
    $("#left-form").fadeIn(100);
    $("#right-list").css("grid-column","2/3");
  });
  
});
