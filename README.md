# Description
Speedwagon Algorithm is a basic and easy to use/implement asymmetric encryption algorithm includes methods named *key_part1()*, *key_part2()*, *encrypt()*,*decrypt()*, *keyed_encrypt()* and *keyed_decrypt()*.

*key_part1()* generates 32-bit key with a specific type.
*key_part2()* generates 32-bit key with another specific type.
*key_part1()* and *key_part2()* became a main key by concatenation.
*encrypt()* encrypts the data given by parameter according to Speedwagon Algorithm without any key.
*decrypt()* decrypts data which is encrypted by Speedwagon Algorithm without any key.
*keyed_encrypt()* encrypts the data given by parameter according to Speedwagon Algorithm with a main key.
*keyed_decrypt()* decrypts data which is encrypted by Speedwagon Algorithm with a main key.


## Installation

    pip install speedwagon_algorithm
  or
  
    pip3 install speedwagon_algorithm


## Usage
```python
from speedwagon_algorithm import key_part1,key_part2,encrypt,decrypt,keyed_encrypt,keyed_decrypt
    
#this data gonna be encrypted without key
example_data1 =  "Your face seems to be asking \"Who's this?\", so let me introduce myself! I'm the meddling Speedwagon!"
encrypted_data1 = encrypt(example_data1) #Content of encrypted_data1 (fix): iaxg3fjafhsfjmbv3auxy5hq65ajmbslv65a65aadsslvjmbpdfg3fjmbyua65ajmbuxyslvagsavahidoysjmb"""hjlapag3f'''slvjmbpdfapaavaslv???""",,,jmbslvg3fjmbasg65apdfjmbads65ajmbavahidpdfhsfg3fgiajaf5hq65ajmbadsvsgslv65aasgv3a!!!jmbkjj'''adsjmbpdfapa65ajmbads65agiagiaasgavahidoysjmb5s5yus65a65agiaovcuxyoysg3fhid!!!
decrypted_data1 = decrypt(encrypted_data1)


#this data gonna be encrypted with key
example_data2 =  "Stop, everyone! If you touch this gentleman, I, Speedwagon, won't forgive you!"
    
key1 = key_part1()
key2 = key_part2()
main_key = key1 + key2
    
encrypted_data2 = keyed_encrypt(example_data2,main_key) #Content of encrypted_data2 (will be change if main_key changed): 5s5ytdovcyuskfjyusyus65agia65ayusyus65agiaslvslvovcoysytdoysoyskfjslvgiakfj65aovcovcoysytdyuskfjgiatysf8sghcg3f65af8sg3f54kofdgvxkghofdghcghc65akhy65akghf8skhy65a65agvxkghgvxtys54ktysf8stys54kkhypdfg3fyus,,,jmb65a8dq65ahsfvsgg3fhid65a!!!jmbkjjv3ajmbvsgg3fjafjmbpdfg3fjaf5hqapajmbpdfapaavaslvjmboys65ahidpdfasg65aadsuxyhid,,,jmbkjj,,,jmb5s5yus65a65agiaovcuxyoysg3fhid,,,jmbovcg3fhid'''pdfjmbv3ag3fhsfoysava8dq65ajmbvsgg3fjaf!!!
decrypted_data2 = keyed_decrypt(encrypted_data2,main_key)




#Legal Procedure Line: Contents of example_data1 and example_data2 in this example script, come from JoJo's Bizarre Encyclopedia (https://jojowiki.com), and must be attributed to its authors if you are using it on another wiki or web page, as specified in the license.
```
    
## Notice
Encrypting your sensitive data multiple times is recommended by developer.
