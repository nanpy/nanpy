template <typename T> class SlimVector {

    private:
        int size;
        int cur_size;
        T *v;

    public:
        SlimVector(int s=0) : size(s), v((T*)malloc(sizeof(T) * size)) {
            for(int i = 0; i < size; i++)
                v[i] = 0;
            cur_size = 0;
        }

        SlimVector(T *x, int s) : size(s), v((T*)malloc(sizeof(T) * size)) {
            size = s;
            for(int i = 0; i < size; i++)
                v[i] = x[i];
        }

        void insert(T el) {
            this->insert(cur_size, el);
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

        ~SlimVector() {
            free(v);
        }

};

/*  template<typename T>
   void vecTor<T>::printvec() const
    {
     cout<<"Vector is:\n";
      for(int i=0; i<size; i++)
      cout<< v[i] <<" ";
      cout<<"\n";
    }

int main()
{
  int a[3]= {3,5,7};

  vecTor<int> v1(3);

  v1=vecTor<int>(a,3);   // this call produces seg. fault

  //v1.vecTorset(a,3);    //this call works fine

  v1.printvec();

  return 0; */
