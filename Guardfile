# Compile the application css file.
guard 'sass',
    :input => 'application/Source/Sass',
    :output => 'static',
    :all_on_start => true,
    :style => :compressed

# Compile the application javascript file.
guard 'sprockets',
    :destination => 'static',
    :minify => 'yes',
    :asset_paths => ['Source'],
    :root_file => 'application/application.js' do
    watch(%r{^application/Source/*/.*\.js$})
    watch(%r{^application/Source/*/.*\.ejs$})
end

guard 'sprockets',
    :destination => 'static',
    :minify => 'yes',
    :root_file => 'site/javascript/pulse.js' do
    watch(%r{^site/javascript/.*\.js$})
end

# Compile HAML templates into the Source directory.
guard 'haml',
    :output => 'application/Source/Templates',
    :input => 'application/Templates',
    :run_at_start => true,
    :haml_options => {:escape_attrs => false } do
    watch %r{^application/Templates/.*(\.haml)}
end

guard 'haml',
    :ouput => 'site/templates',
    :input => 'site/templates',
    :run_at_start => true,
    :force_html => true,
    :haml_options => {:escape_attrs => false } do
    watch %r{^site/templates/.*(\.haml)}
end

# Compile the landing page css file.
guard 'sass',
    :input => 'site/sass',
    :output => 'static',
    :all_on_start => true,
    :style => :compressed