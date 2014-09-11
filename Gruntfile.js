module.exports = function(grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    config: grunt.file.readJSON('package.json').config,
    compass: {
      dist: {
        options: {
          cssDir: '<%= config.stylesDir %>/',
          imagesDir: '<%= config.imagesDir %>/',
          fontsDir: '<%= config.fontsDir %>/',

        }
      }
    },


    concat: {
      app: {
        src: ['<%= config.scriptsDevDir %>/**/*.js'],
        dest: '<%= config.distDir %>/<%= pkg.name %>.js'
      },
      vendor: {
        src: [
          '<%= config.staticDir %>/vendor/jquery/dist/jquery.min.js',
          '<%= config.staticDir %>/vendor/lodash/dist/lodash.min.js',
          '<%= config.staticDir %>/vendor/modernizer/modernizer.js',
        ],
        dest: '<%= config.distDir %>/vendor.js'
      }
    },


    uglify: {
      options: {
        // sourceMap: true,
        // sourceMapIncludeSources: true,
        banner: '/*! <%= pkg.name %>  */\n'
      },
      dist: {
        files: {
          '<%= config.distDir %>/<%= pkg.name %>.min.js': ['<%= concat.app.dest %>'],
          '<%= config.distDir %>/vendor.min.js': ['<%= concat.vendor.dest %>'],
        }
      }
    },


    cssmin: {
      combine: {
        files: {
          '<%= config.distDir %>/<%= pkg.name %>.min.css': ['<%= config.stylesDir %>/**/*.css'],
        }
      },
    },


    // Add tasks here to run on every file saved change, as you would do for coffeescript, style preproccesors
    watch: {
      compass: {
        files: '<%= config.stylesDir %>/**/*.{scss,sass}',
        tasks: ['compass']
      },
    }

  });


  grunt.registerTask('build',
    ['compass', 'cssmin', 'concat', 'uglify']);


  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-compass');
  grunt.loadNpmTasks('grunt-contrib-cssmin');


  grunt.registerTask('default',['watch']);

};
