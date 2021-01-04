$().ready(function() {
  $("#registration").validate({
    rules: {
      username_input: {
        required : true,
        minlength: 3

      },

      email_input: {
        required: true, 
        email: true
      },
      password_input: {
        required: true, 
        minlength: 5, 
 
      },
      confirm_pw: {
        required: true, 
        equalTo: "#password"
      }

    },
    messages: {
      username_input: {
        required: "Please provide a username",
        minlength: "Username must containe more than 3 characters"
      },
      email_input: {
        required: "Please enter an email address",
        email: "Please add a valid email address"
      },
      password_input: {
        required: "Please add a password",
        minlength: "Password must be a minimum of 5 characters"
      },
      confirm_pw: {
        required: "reconfirm you password",
        equalTo: "Password does not match"
      }
    }

  });
});