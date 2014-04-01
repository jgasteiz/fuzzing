module.exports = function(grunt) {

	require("matchdep").filterDev("grunt-*").forEach(grunt.loadNpmTasks);

	grunt.initConfig({
		pkg: grunt.file.readJSON('package.json'),
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
			options: {
				scss: true,
				url: '../img',
				'sprite-namespace' : 'sprite',
				retina: true
			},
			dev: {
				src : 'fuzzing/static/sprite',
				dest: 'fuzzing/static/scss'
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
	grunt.registerTask('default', ['glue:dev', 'sass:dev', 'concurrent:watch']);
};
