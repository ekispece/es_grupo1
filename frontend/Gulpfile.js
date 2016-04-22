var gulp = require('gulp');
var less = require('gulp-less');

gulp.task('build-less', function () {
    return gulp.src('less/main.less')
        .pipe(less())
        .pipe(gulp.dest('css'))
});

gulp.task('default', ['build-less']);
