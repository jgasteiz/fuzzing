module.exports = function(grunt) {

	require("matchdep").filterDev("grunt-*").forEach(grunt.loadNpmTasks);

	grunt.initConfig({
		pkg: grunt.file.readJSON('package.json'),
		glueOptions: '--scss --namespace= --sprite-namespace=sprite --retina --recursive',
		devStaticDir: 'fuzzing/static',
		sass: {
			dev: {
				options: {
					style: "expanded"
				},
				files: {
					'<%= devStaticDir %>/css/cms.css': '<%= devStaticDir %>/scss/cms/cms.scss',
					'<%= devStaticDir %>/css/larevolta.css': '<%= devStaticDir %>/scss/themes/larevolta.scss',
					'<%= devStaticDir %>/css/taller.css': '<%= devStaticDir %>/scss/themes/taller.scss'
				}
			}
		},
		glue: {
			larevolta: {
				files : [{
					src : 'fuzzing/static/sprite/',
					img : 'fuzzing/static/img/',
					css : 'fuzzing/static/scss/themes/larevolta/'
				}],
				options: {
					retina: true,
					recursive: true,
					"sprite-namespace": "sprite",
					url: '../img/'
				}
			}
		},
		watch: {
			sassDev: {
				files: ['<%= devStaticDir %>/scss/**/*.scss'],
				tasks: ['sass:dev', 'notify:css']
			},
			images: {
				files: ['<%= devStaticDir %>/sprite/**/*'],
				tasks: ['glue:dev']
			}
		},
		concurrent: {
			watch: {
				tasks: ['watch:sassDev', 'watch:images'],
				options: {
					logConcurrentOutput: true
				}
			}
		},
		csso: {
			release: {
				options: {
				    report: 'min'
				},
			  	files: {
			    	'<%= devStaticDir %>/css/cms.css': '<%= devStaticDir %>/css/cms.css',
					'<%= devStaticDir %>/css/larevolta.css': '<%= devStaticDir %>/css/larevolta.css',
					'<%= devStaticDir %>/css/taller.css': '<%= devStaticDir %>/css/taller.css'
			  	}
			}
		},
		notify: {
			css: {
				options: {
					title: 'Task Complete',
					message: 'CSS is ready'
				}
			}
		}
	});

	// Default task(s).
	grunt.registerTask('default', ['glue:larevolta', 'sass:dev', 'concurrent:watch']);
};
