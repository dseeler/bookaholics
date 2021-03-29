function validateName(){
    let valid = true;

    if ($("#first_name").val().length < 1){
        $("#first_name").attr("style", "border: 1px solid red");
        $("#first-name-error").html("Can't be empty!");
        valid = false;
    }

    if ($("#last_name").val().length < 1){
        $("#last_name").attr("style", "border: 1px solid red");
        $("#last-name-error").html("Can't be empty!");
        valid = false;
    }

    if ($("#first_name").val().length > 20){
        $("#first_name").attr("style", "border: 1px solid red");
        $("#first-name-error").html("Must be <=20 characters");
        valid = false;
    }

    if ($("#last_name").val().length > 20){
        $("#last_name").attr("style", "border: 1px solid red");
        $("#last-name-error").html("Must be <=20 characters");
        valid = false;
    }

    if (valid){
        $("#name-form").submit();
    }
}

function clearFirstName(){
    $("#first_name").attr("style", "border: 1px solid black");
    $("#first-name-error").html("");
}


function clearLastName(){
    $("#last_name").attr("style", "border: 1px solid black");
    $("#last-name-error").html("");
}

function validatePassword(){
    let valid = true;

    if ($("#password").val().length < 8){
        $("#password").attr("style", "border: 1px solid red");
        $("#password-error").html("Must be >= 8 characters");
        valid = false;
    }

    if ($("#password").val().length > 20){
        $("#password").attr("style", "border: 1px solid red");
        $("#password-error").html("Must be <= 20 characters");
        valid = false;
    }

    if (!/[^a-zA-Z]/.test($("#password").val()) && !/\d/.test($("#password").val())){
        $("#password").attr("style", "border: 1px solid red");
        $("#password-error").html("Needs letters and digits");
        valid = false;
    }

    if ($("#password").val() != $("#password_confirmation").val()){
        $("#password").attr("style", "border: 1px solid red");
        $("#password_confirmation").attr("style", "border: 1px solid red");
        $("#password-error").html("Passwords do not match");
        valid = false;
    }

    if (valid){
        $("#password-form").submit();
    }
}

function clearPassword(){
    $("#password").attr("style", "border: 1px solid black");
    $("#password_confirmation").attr("style", "border: 1px solid black");
    $("#password-error").html("");
}

function validatePhone(){
    let valid = true;

    if ($("#phone").val().length != 10){
        $("#phone").attr("style", "border: 1px solid red");
        $("#phone-error").html("Must be 10 characters");
        valid = false;
    }

    if (/\D/.test($("#phone").val())){
        $("#phone").attr("style", "border: 1px solid red");
        $("#phone-error").html("Only digits allowed");
        valid = false;
    }

    if (valid){
        $("#phone-form").submit();
    }
}

function clearPhone(){
    $("#phone").attr("style", "border: 1px solid black");
    $("#phone-error").html("");
}

function validateAddress(){
    let valid = true;

    if ($("#street").val().length < 1){
        $("#street").attr("style", "border: 1px solid red");
        $("#street-error").html("Can't be empty");
        valid = false;
    }

    if ($("#city").val().length < 1){
        $("#city").attr("style", "border: 1px solid red");
        $("#city-error").html("Can't be empty");
        valid = false;
    }

    if ($("#state").val().length != 2){
        $("#state").attr("style", "border: 1px solid red");
        $("#state-error").html("Must be an abbreviation");
        valid = false;
    }

    if ($("#zip_code").val().length != 5){
        $("#zip_code").attr("style", "border: 1px solid red");
        $("#zip-code-error").html("Must be 5 characters");
        valid = false;
    }

    if (/[^a-zA-Z]/.test($("#city").val())){
        $("#city").attr("style", "border: 1px solid red");
        $("#city-error").html("Only letters allowed");
        valid = false;
    }


    if (/[^a-zA-Z]/.test($("#state").val())){
        $("#state").attr("style", "border: 1px solid red");
        $("#state-error").html("Only letters allowed");
        valid = false;
    }

    if (/\D/.test($("#zip_code").val())){
        $("#zip_code").attr("style", "border: 1px solid red");
        $("#zip-code-error").html("Only digits allowed");
        valid = false;
    }

    if (valid){
        $("#address-form").submit();
    }
}

function clearStreet(){
    $("#street").attr("style", "border: 1px solid black");
    $("#street-error").html("");
}


function clearCity(){
    $("#city").attr("style", "border: 1px solid black");
    $("#city-error").html("");
}

function clearState(){
    $("#state").attr("style", "border: 1px solid black");
    $("#state-error").html("");
}

function clearZipCode(){
    $("#zip_code").attr("style", "border: 1px solid black");
    $("#zip-code-error").html("");
}

function validateCard(){
    let valid = true;

    if ($("#card_num").val().length != 16){
        $("#card_num").attr("style", "border: 1px solid red");
        $("#card-num-error").html("Must be 16 characters");
        valid = false;
    }

    if ($("#card_exp").val().length != 5){
        $("#card_exp").attr("style", "border: 1px solid red");
        $("#card-exp-error").html("Must be in MM/YY format");
        valid = false;
    }

    if ($("#card_code").val().length != 3){
        $("#card_code").attr("style", "border: 1px solid red");
        $("#card-code-error").html("Must be 3 characters");
        valid = false;
    }

    if (/\D/.test($("#card_num").val())){
        $("#card_num").attr("style", "border: 1px solid red");
        $("#card-num-error").html("Only digits allowed");
        valid = false;
    }

    if (/\D/.test($("#card_code").val())){
        $("#card_code").attr("style", "border: 1px solid red");
        $("#card-code-error").html("Only digits allowed");
        valid = false;
    }

    if (valid){
        $("#card-form").submit();
    }
}

function clearCardNum(){
    $("#card_num").attr("style", "border: 1px solid black");
    $("#card-num-error").html("");
}


function clearCardExp(){
    $("#card_exp").attr("style", "border: 1px solid black");
    $("#card-exp-error").html("");
}

function clearCardCode(){
    $("#card_code").attr("style", "border: 1px solid black");
    $("#card-code-error").html("");
}

function editName(){
    if ($("#edit-name-button").val() == 0){
        closeOtherTabs("name");
        $("#edit-name-option").animate({
            height: "200px"
        });
        $("#edit-name-form").show();
        $("#edit-name-button").html("Cancel");
        $("#edit-name-button").val(1);
    }
    else{
        $("#edit-name-option").animate({
            height: "100px"
        });
        $("#edit-name-form").hide();
        $("#edit-name-button").html("Edit");
        $("#edit-name-button").val(0);
    }
}

function editPassword(){
    if ($("#edit-password-button").val() == 0){
        closeOtherTabs("password");
        $("#edit-password-option").animate({
            height: "150px"
        });
        $("#edit-password-form").show();
        $("#edit-password-button").html("Cancel");
        $("#edit-password-button").val(1);
    }
    else{
        $("#edit-password-option").animate({
            height: "100px"
        });
        $("#edit-password-form").hide();
        $("#edit-password-button").html("Edit");
        $("#edit-password-button").val(0);
    }
}

function editPhone(){
    if ($("#edit-phone-button").val() == 0){
        closeOtherTabs("phone");
        $("#edit-phone-option").animate({
            height: "165px"
        });
        $("#edit-phone-form").show();
        $("#edit-phone-button").html("Cancel");
        $("#edit-phone-button").val(1);
    }
    else{
        $("#edit-phone-option").animate({
            height: "100px"
        });
        $("#edit-phone-form").hide();
        $("#edit-phone-button").html("Edit");
        $("#edit-phone-button").val(0);
    }
}

function editAddress(){
    if ($("#edit-address-button").val() == 0){
        closeOtherTabs("address");
        $("#edit-address-option").animate({
            height: "272px"
        });
        $("#edit-address-form").show();
        $("#edit-address-button").html("Cancel");
        $("#edit-address-button").val(1);
    }
    else{
        $("#edit-address-option").animate({
            height: "100px"
        });
        $("#edit-address-form").hide();
        $("#edit-address-button").html("Edit");
        $("#edit-address-button").val(0);
    }
}

function editCard(){
    if ($("#edit-card-button").val() == 0){
        closeOtherTabs("card");
        $("#edit-card-option").animate({
            height: "235px"
        });
        $("#edit-card-form").show();
        $("#edit-card-button").html("Cancel");
        $("#edit-card-button").val(1);
    }
    else{
        $("#edit-card-option").animate({
            height: "100px"
        });
        $("#edit-card-form").hide();
        $("#edit-card-button").html("Edit");
        $("#edit-card-button").val(0);
    }
}

function closeOtherTabs(selected){
    switch (selected){
        case "name":
            if ($("#edit-card-button").val() == 1){
                $("#edit-card-option").animate({
                    height: "100px"
                });
                $("#edit-card-form").hide();
                $("#edit-card-button").html("Edit");
                $("#edit-card-button").val(0);
            }
            if ($("#edit-password-button").val() == 1){
                $("#edit-password-option").animate({
                    height: "100px"
                });
                $("#edit-password-form").hide();
                $("#edit-password-button").html("Edit");
                $("#edit-password-button").val(0);
            }
            if ($("#edit-address-button").val() == 1){
                $("#edit-address-option").animate({
                    height: "100px"
                });
                $("#edit-address-form").hide();
                $("#edit-address-button").html("Edit");
                $("#edit-address-button").val(0);
            }
            if ($("#edit-phone-button").val() == 1){
                $("#edit-phone-option").animate({
                    height: "100px"
                });
                $("#edit-phone-form").hide();
                $("#edit-phone-button").html("Edit");
                $("#edit-phone-button").val(0);
            }
        break;
        case "password":
            if ($("#edit-card-button").val() == 1){
                $("#edit-card-option").animate({
                    height: "100px"
                });
                $("#edit-card-form").hide();
                $("#edit-card-button").html("Edit");
                $("#edit-card-button").val(0);
            }
            if ($("#edit-name-button").val() == 1){
                $("#edit-name-option").animate({
                    height: "100px"
                });
                $("#edit-name-form").hide();
                $("#edit-name-button").html("Edit");
                $("#edit-name-button").val(0);
            }
            if ($("#edit-address-button").val() == 1){
                $("#edit-address-option").animate({
                    height: "100px"
                });
                $("#edit-address-form").hide();
                $("#edit-address-button").html("Edit");
                $("#edit-address-button").val(0);
            }
            if ($("#edit-phone-button").val() == 1){
                $("#edit-phone-option").animate({
                    height: "100px"
                });
                $("#edit-phone-form").hide();
                $("#edit-phone-button").html("Edit");
                $("#edit-phone-button").val(0);
            }
        break;
        case "phone":
            if ($("#edit-card-button").val() == 1){
                $("#edit-card-option").animate({
                    height: "100px"
                });
                $("#edit-card-form").hide();
                $("#edit-card-button").html("Edit");
                $("#edit-card-button").val(0);
            }
            if ($("#edit-password-button").val() == 1){
                $("#edit-password-option").animate({
                    height: "100px"
                });
                $("#edit-password-form").hide();
                $("#edit-password-button").html("Edit");
                $("#edit-password-button").val(0);
            }
            if ($("#edit-address-button").val() == 1){
                $("#edit-address-option").animate({
                    height: "100px"
                });
                $("#edit-address-form").hide();
                $("#edit-address-button").html("Edit");
                $("#edit-address-button").val(0);
            }
            if ($("#edit-name-button").val() == 1){
                $("#edit-name-option").animate({
                    height: "100px"
                });
                $("#edit-name-form").hide();
                $("#edit-name-button").html("Edit");
                $("#edit-name-button").val(0);
            }
        break;
        case "address":
            if ($("#edit-card-button").val() == 1){
                $("#edit-card-option").animate({
                    height: "100px"
                });
                $("#edit-card-form").hide();
                $("#edit-card-button").html("Edit");
                $("#edit-card-button").val(0);
            }
            if ($("#edit-password-button").val() == 1){
                $("#edit-password-option").animate({
                    height: "100px"
                });
                $("#edit-password-form").hide();
                $("#edit-password-button").html("Edit");
                $("#edit-password-button").val(0);
            }
            if ($("#edit-name-button").val() == 1){
                $("#edit-name-option").animate({
                    height: "100px"
                });
                $("#edit-name-form").hide();
                $("#edit-name-button").html("Edit");
                $("#edit-name-button").val(0);
            }
            if ($("#edit-phone-button").val() == 1){
                $("#edit-phone-option").animate({
                    height: "100px"
                });
                $("#edit-phone-form").hide();
                $("#edit-phone-button").html("Edit");
                $("#edit-phone-button").val(0);
            }
        break;
        case "card":
            if ($("#edit-name-button").val() == 1){
                $("#edit-name-option").animate({
                    height: "100px"
                });
                $("#edit-name-form").hide();
                $("#edit-name-button").html("Edit");
                $("#edit-name-button").val(0);
            }
            if ($("#edit-password-button").val() == 1){
                $("#edit-password-option").animate({
                    height: "100px"
                });
                $("#edit-password-form").hide();
                $("#edit-password-button").html("Edit");
                $("#edit-password-button").val(0);
            }
            if ($("#edit-address-button").val() == 1){
                $("#edit-address-option").animate({
                    height: "100px"
                });
                $("#edit-address-form").hide();
                $("#edit-address-button").html("Edit");
                $("#edit-address-button").val(0);
            }
            if ($("#edit-phone-button").val() == 1){
                $("#edit-phone-option").animate({
                    height: "100px"
                });
                $("#edit-phone-form").hide();
                $("#edit-phone-button").html("Edit");
                $("#edit-phone-button").val(0);
            }
        break;
    }
    
}
