const mix = require('laravel-mix');

mix.js('firstapp/templates/firstapp/assets/js/app.js', 'firstapp/static/assets/js')
    .vue();
    // .sass('resources/sass/app.scss', 'public/css');
