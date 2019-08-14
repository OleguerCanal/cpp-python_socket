cd cpp/
rm -rf build/
mkdir build/
cd build/
# cmake ..
cmake -DUSE_OPENCV=OFF ..
echo "Finished cmake .."
make -j
cd ../..