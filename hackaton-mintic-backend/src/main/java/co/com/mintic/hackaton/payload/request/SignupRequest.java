package co.com.mintic.hackaton.payload.request;

import java.sql.Date;
import java.util.Set;

import javax.persistence.Column;
import javax.validation.constraints.Email;
import javax.validation.constraints.NotBlank;
import javax.validation.constraints.Size;

public class SignupRequest {
	@NotBlank
	@Size(min = 3, max = 20)
	private String username;

	@NotBlank
	@Size(max = 50)
	@Email
	private String email;

	private Set<String> role;

	@NotBlank
	@Size(max = 150)
	private String name;

	private Long cedula;

	@NotBlank
	@Size(min = 6, max = 40)
	private String password;

	@NotBlank
	@Size(max = 120)
	@Column(name = "address")
	private String address;

	@NotBlank
	@Size(max = 1)
	@Column(name = "gender")
	private String gender;

	@Column(name = "birthdate")
	private Date birthdate;

	public SignupRequest(@NotBlank @Size(min = 3, max = 20) String username,
			@NotBlank @Size(max = 50) @Email String email, Set<String> role, @NotBlank @Size(max = 150) String name,
			Long cedula, @NotBlank @Size(min = 6, max = 40) String password, @NotBlank @Size(max = 120) String address,
			@NotBlank @Size(max = 1) String gender, Date birthdate) {
		super();
		this.username = username;
		this.email = email;
		this.role = role;
		this.name = name;
		this.cedula = cedula;
		this.password = password;
		this.address = address;
		this.gender = gender;
		this.birthdate = birthdate;
	}

	public String getAddress() {
		return address;
	}

	public void setAddress(String address) {
		this.address = address;
	}

	public String getGender() {
		return gender;
	}

	public void setGender(String gender) {
		this.gender = gender;
	}

	public Date getBirthdate() {
		return birthdate;
	}

	public void setBirthdate(Date birthdate) {
		this.birthdate = birthdate;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public Long getCedula() {
		return cedula;
	}

	public void setCedula(Long cedula) {
		this.cedula = cedula;
	}

	public String getUsername() {
		return username;
	}

	public void setUsername(String username) {
		this.username = username;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public String getPassword() {
		return password;
	}

	public void setPassword(String password) {
		this.password = password;
	}

	public Set<String> getRole() {
		return this.role;
	}

	public void setRole(Set<String> role) {
		this.role = role;
	}
}
