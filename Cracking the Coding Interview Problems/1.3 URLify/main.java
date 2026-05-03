public class main {
    static char[] solution(char[] arrInput, int len) {
        int counter = 0;
        for (int i = 0; i < len; i++){
            if (arrInput[i] == ' '){
                counter++;
            }
        }

        int i = len-1+(counter*2);
        int j = len-1;
        while (j >= 0){
            char c = arrInput[j];
            if (c != ' '){
                arrInput[i] = c;
            }
            else{
                arrInput[i] = '0';
                i--;
                arrInput[i] = '2';
                i--;
                arrInput[i] = '%';
            }
            i--;
            j--;
        }
        return arrInput;
    }
    
    
    public static void main(String[] args) {
        char[] arrInput = {'M','r',' ','J','o','h','n',' ','S','m','i','t','h',' ',' ',' ',' '};
        int length = 13;
        System.out.println(solution(arrInput, length));
    }
}