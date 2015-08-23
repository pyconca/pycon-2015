var gulp        = require('gulp'),
    less        = require('gulp-less'),
    minifycss   = require('gulp-minify-css');

//------------------------------------------------------------------------------
// less
//------------------------------------------------------------------------------

gulp.task('less', function() {
    return gulp.src('./static/css/app.less')
        .pipe(less())
        .pipe(minifycss())
        .pipe(gulp.dest('./static/css'));
});

gulp.task('watch-less', function() {
    gulp.watch('static/css/**/*.less', ['less']);
});

//------------------------------------------------------------------------------
// default
//------------------------------------------------------------------------------

gulp.task('build', ['less']);
gulp.task('default', ['build', 'watch-less']);
