package br.edu.atitus.apisample.services;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.springframework.stereotype.Service;

import br.edu.atitus.apisample.entities.UserEntity;
import br.edu.atitus.apisample.repositories.UserRepository;

@Service
public class UserService {
	
	private final UserRepository repository;
	
	//pegando por DI
	public UserService(UserRepository repository) {
		super();
		this.repository = repository;
	}

	public UserEntity save(UserEntity newUser) throws Exception {
		//validar regras de negocio
		if(newUser == null)
			throw new Exception("O objeto está nulo.");
		
		if(newUser.getName() == null || newUser.getName().isEmpty())
			throw new Exception("Nome inválido.");
		newUser.setName(newUser.getName().trim());
		
		if(newUser.getEmail() == null || newUser.getEmail().isEmpty() || !validate(newUser.getEmail()))
			throw new Exception("Email inválido.");
		newUser.setEmail(newUser.getEmail().trim());
		
		if(repository.existsByEmail(newUser.getEmail()))
			throw new Exception("E-mail já existe.");
		
		//invocar o repositorio
		this.save(newUser);
		
		return newUser;
	}

	public static boolean validate(String emailStr) {
		Pattern VALID_EMAIL_ADDRESS_REGEX = Pattern.compile("^[A-Z0-9._%+-]+@[A-Z0-9.-]+\\.[A-Z]{2,6}$", Pattern.CASE_INSENSITIVE);
        Matcher matcher = VALID_EMAIL_ADDRESS_REGEX.matcher(emailStr);
        return matcher.matches();
	}
}
