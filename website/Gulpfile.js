// var gulp = require('gulp');
// var less = require('gulp-less');
// var watch = require('gulp-watch')
//
// gulp.task('build-less', function () {
//     return gulp.src('less/main.less')
//         .pipe(less())
//         .pipe(gulp.dest('css'))
// });
//
// // gulp.task('watch', function () {
// //     return gulp.src('less/main.less')
// //         .pipe(watch('less/*.less'))
// //         .pipe(less())
// //         .pipe(gulp.dest('css'))
// // });
//
// gulp.task('default', ['build-less']);
var elixir = require('laravel-elixir');

elixir.config.assetsPath = ".";
elixir.config.publicPath = ".";

elixir(function(mix){
    mix.less([
        '../bower_components/bootstrap/less/bootstrap.less',
        '../bower_components/font-awesome/less/font-awesome.less',
        'main.less'
    ]);
})
