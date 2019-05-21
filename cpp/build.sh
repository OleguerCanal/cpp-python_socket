rm -rf build/
mkdir build/
cd build/
cmake ..
# cmake -D -USE_OPENCV=OFF ..
echo "Finished cmake .."
make -j
cd ..