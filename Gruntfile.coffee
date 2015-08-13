module.exports = (grunt) ->
    require('time-grunt') grunt

    grunt.config.init
        clean:
            dist: [
                'todolist/static/dist'
            ]


        coffee:
            app:
                files:
                    'todolist/static/dist/javascript/app.js': [
                        'todolist/static/coffee/**/*.coffee'
                    ]

        ect:
            angularDebug:
                options:
                    root: 'todolist/static'
                    variables:
                        isDebug: yes
                expand: yes
                flatten: no
                cwd: 'todolist/static/templates/angular'
                src: '**/*.html'
                dest: 'todolist/static/dist/templates'
                ext: '.html'

        concurrent:
            devCompile:
                ###
                Compile sass, coffee script and render template and copy fonts.
                ###
                tasks: [
                    'coffee'
                    'ect:angularDebug'
                ]
                options:
                    logConcurrentOutput: yes
            develop:
                ###
                Watch files and run develop server.
                ###
                tasks: [
                    'watch'
                    'shell:pyramid'
                ]
                options:
                    logConcurrentOutput: yes

        watch:
            coffeeApp:
                files: ['todolist/static/coffee/**/*.coffee']
                tasks: ['coffee:app']
                options:
                    spawn: no
            ectAngular:
                files: [
                    'todolist/static/templates/angular/**/*.html'
                    'todolist/static/templates/shared/**/*.html'
                ]
                tasks: ['ect:angularDebug']

        symlink:
            bower:
                files: [
                    {
                        expand: yes
                        overwrite: no
                        src: ['bower_components']
                        dest: 'todolist/static/dist'
                        filter: 'isDirectory'
                    }
                ]


        shell:
            pyramid:
                options:
                    stdin: no
                    stdout: yes
                    stderr: yes
                command: 'pserve development.ini --reload'
            checkDependencies:
                options:
                    stdin: no
                    stdout: yes
                    stderr: yes
                command:
                    """
                        echo check dependencies
                        npm install
                        bower install
                        python setup.py develop
                    """


    # -----------------------------------
    # register task
    # -----------------------------------
    grunt.registerTask 'dev', [
        'shell:checkDependencies'
        'clean:dist'
        'symlink:bower'
        'concurrent:devCompile'
        'concurrent:develop'
    ]

    # -----------------------------------
    # tasks
    # -----------------------------------
    grunt.loadNpmTasks 'grunt-concurrent'
    grunt.loadNpmTasks 'grunt-contrib-clean'
    grunt.loadNpmTasks 'grunt-contrib-coffee'
    grunt.loadNpmTasks 'grunt-contrib-compass'
    grunt.loadNpmTasks 'grunt-contrib-symlink'
    grunt.loadNpmTasks 'grunt-contrib-watch'
    grunt.loadNpmTasks 'grunt-ect'
    grunt.loadNpmTasks 'grunt-shell'
