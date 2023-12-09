// colection of functions for opening the various pages of the application

function open_review(page)
{
    console.log(page);
    window.location.href = "/review/"+page;
}

function open_rollercoaster(rollercoaster)
{
    console.log(rollercoaster);
    window.location.href = "/rollercoaster/"+rollercoaster;
}

function open_profile(profile)
{
    console.log(profile);
    window.location.href = "/profile/"+profile;
}