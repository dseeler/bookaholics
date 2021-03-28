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
            height: "200px"
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