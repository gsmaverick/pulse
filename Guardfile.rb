# Compile the application css file.
guard 'sass',
    :input => 'application/Source/Sass',
    :output => 'static',
    :all_on_start => true

# Compile the application javascript file.
guard 'sprockets',
    :destination => 'static',
    :minify => 'yes',
    :asset_paths => ['Source'],
    :root_file => 'application/application.js' do
    watch(%r{^application/Source/*/.*\.js$})
    watch(%r{^application/Source/*/.*\.ejs$})
end

# Compile HAML templates into the Source directory.
guard 'haml',
    :output => 'application/Source/Templates',
    :input => 'application/Templates',
    :run_at_start => true,
    :haml_options => {:escape_attrs => false } do
    watch %r{^application/Templates/.*(\.haml)}
end