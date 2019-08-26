$("#incorrect").on("click", function() {
  // $(".prog-result").html("");
  $('#incorrect').trigger('focus')
  $("ul").html("");
  $("#progress").addClass("hide");
  totaLtime = 0;
});

function save_name() {
  username = $("#name").val();
  localStorage.setItem("username", username)
}


var inputs = $("form#contactForm input, form#contactForm textarea");

var validateInputs = function validateInputs(inputs) {
  var validForm = true;
  inputs.each(function(index) {
    var input = $(this);
    if (!input.val() || (input.type === "grade" && !input.is(':checked'))) {
      $("#sendMessageButton1").attr("disabled", "disabled");
      validForm = false;
    }
  });
  return validForm;
}


inputs.each(function() {
  var input = $(this);
  if (input.type === "grade") {
    input.change(function() {
      if (validateInputs(inputs)) {
        $("#sendMessageButton1").removeAttr("disabled");
      }
    });
  }
  else {
    input.keyup(function() {
      if (validateInputs(inputs)) {
        $("#sendMessageButton1").removeAttr("disabled");
      }
    });
  }
});





















// function req_data(answers) {
//   var xhttp = new XMLHttpRequest();
//   xhttp.onreadystatechange = function() {
//     if (this.readyState == 4 && this.status == 200) {
//       document.getElementById("answer").innerHTML = this.responseText;
//       myResponse = JSON.parse(this.responseText);
//         if ((myResponse.results) == True) {
//     }
//     else {
//       return false
//     }
//   };
//   xhttp.open("GET", "{{url_for('get_question') }}" + "?question=" + "answers" + answers  , true);
//   xhttp.send();
// }
// }


// $("#answerId").on("click", function() {

//     req_data($("#answer_box").val());

// });
