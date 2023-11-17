from colorama import Fore, Back, Style, init, deinit

# эта функция инициализирует Colorama. Обычно он вызывается в начале вашего проэета. Параметры позволяют настроить поведение колорамы.

init()

#В этом примере Fore.RED, Back.GREEN и Style.BRIGHT используются для установки цвета текста, цвета фона и стиля. 
#Style.RESET_ALL используется для сброса текстовых атрибутов к значениям по умолчанию.
print(f"{Fore.RED}{Back.GREEN}{Style.BRIGHT}This is a colored text!{Style.RESET_ALL}")

#эта функция деинициализирует Colorama и используется для сброса настроек цвета терминала в исходное состояние.
deinit()


