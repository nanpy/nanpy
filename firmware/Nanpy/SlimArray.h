#ifndef SLIM_ARRAY
#define SLIM_ARRAY

#include <Arduino.h>

namespace nanpy {
    template <typename T> class SlimArray {

        private:

            int size;
            int cur_size;
            T *v;

        public:

            SlimArray(int s=0) : size(s), v((T*)malloc(sizeof(T) * size)) {
                for(int i = 0; i < size; i++)
                    v[i] = 0;
                cur_size = 0;
            }

            SlimArray(T *x, int s) : size(s), v((T*)malloc(sizeof(T) * size)) {
                size = s;
                for(int i = 0; i < size; i++)
                    v[i] = x[i];
            }

            void insert(T el) {
                this->insert(cur_size, el);
            }

            void remove(int pos) {
                if(pos > size - 1)
                    return;

                T* newv = (T*)malloc(sizeof(T) * (size - 1));

                int j = 0;

                for(int i = 0; i < size; i++) {
                    if(i != pos) {
                        newv[j] = v[i];
                        j++;
                    }
                }

                free(v);
                v = newv;
                cur_size--;
                size--;
            }

            void insert(int pos, T el) {
                if(pos > size - 1) {
                    T* newv = (T*)malloc(sizeof(T) * (pos + 1));
                    newv[pos] = el;
                    for(int i = 0; i < size; i++)
                        newv[i] = v[i];
                    free(v);
                    size = pos + 1;
                    v = newv;
                } else {
                    v[pos] = el;
                }
                cur_size++;
            }

            T get(int pos) {
                return v[pos];
            }

            T& operator[] ( int pos ) {
                return v[pos];
            }

            int getSize() {
                return this->size;
            }

            int getLastIndex() {
                return (this->cur_size - 1);
            }

            ~SlimArray() {
                free(v);
            }

    };
}

#endif
