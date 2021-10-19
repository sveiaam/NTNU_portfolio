class SimpleSet{
    public:
        /** Construct empty set **/
        SimpleSet();
        /** Destructor */
        ~SimpleSet();
        /** Insert i into set, return true if the element was inserted, else false **/
        bool insert(int i);
        /** Returns true if i is in the set **/
        bool exists(int i);
        /** Removes i from the set, return true if an element was removed **/
        bool remove(int i);
    private:
        /** Dynamic array containing set elements **/
        int *data;
        /** Current number of elements **/
        int currentSize;
        /** Max capasity of data **/
        int maxSize;       
        
        /** Returns the index where i may be found, else an invalid index. **/
        int find(int i);
        /** Resizes data, superflous elements are dropped. **/
        void resize(int n); 
};