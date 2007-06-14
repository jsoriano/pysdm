libtoolize
echo "Running aclocal..."
aclocal
echo "Running automake.."
automake --add-missing
echo "Running autoconf..."
autoconf
echo "Ready for configure && make && sudo make install"
