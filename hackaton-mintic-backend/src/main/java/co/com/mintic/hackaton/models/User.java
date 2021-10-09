package co.com.mintic.hackaton.models;

import java.sql.Date;
import java.util.HashSet;
import java.util.Set;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.JoinTable;
import javax.persistence.ManyToMany;
import javax.persistence.Table;
import javax.persistence.UniqueConstraint;
import javax.validation.constraints.NotBlank;
import javax.validation.constraints.Size;

@Entity
@Table(name = "usuarios", uniqueConstraints = { @UniqueConstraint(columnNames = "email_usuario"),
		@UniqueConstraint(columnNames = "user_id") })
public class User {
	@Id
	@Column(name = "user_id")
	private Long cedula;

	@NotBlank
	@Size(max = 150)
	@Column(name = "nombre_usuario")
	private String name;

	@NotBlank
	@Size(max = 50)
	@Column(name = "email_usuario")
	private String email;

	@NotBlank
	@Size(max = 20)
	@Column(name = "usuario")
	private String username;

	@NotBlank
	@Size(max = 120)
	@Column(name = "password")
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

	@ManyToMany(fetch = FetchType.LAZY)
	@JoinTable(name = "user_roles", joinColumns = @JoinColumn(name = "user_id"), inverseJoinColumns = @JoinColumn(name = "role_id"))
	private Set<Role> roles = new HashSet<>();

	public User() {
	}

	public User(Long cedula, @NotBlank @Size(max = 150) String name, @NotBlank @Size(max = 50) String email,
			@NotBlank @Size(max = 20) String username, @NotBlank @Size(max = 120) String password,
			@NotBlank @Size(max = 120) String address, @NotBlank @Size(max = 1) String gender,
			@NotBlank @Size(max = 1) Date birthdate, Set<Role> roles) {
		super();
		this.cedula = cedula;
		this.name = name;
		this.email = email;
		this.username = username;
		this.password = password;
		this.address = address;
		this.gender = gender;
		this.birthdate = birthdate;
		this.roles = roles;
	}

	public User(Long cedula, @NotBlank @Size(max = 150) String name, @NotBlank @Size(max = 50) String email,
			@NotBlank @Size(max = 20) String username, @NotBlank @Size(max = 120) String password,
			@NotBlank @Size(max = 120) String address, @NotBlank @Size(max = 1) String gender,
			@NotBlank @Size(max = 1) Date birthdate) {
		super();
		this.cedula = cedula;
		this.name = name;
		this.email = email;
		this.username = username;
		this.password = password;
		this.address = address;
		this.gender = gender;
		this.birthdate = birthdate;
	}
/*
	public User(long cedula, String name, String email, String username, String password, Set<Role> roles) {
		this.cedula = cedula;
		this.name = name;
		this.email = email;
		this.username = username;
		this.password = password;
		this.roles = roles;
	}

	public User(long cedula, String name, String email, String username, String password) {
		this.cedula = cedula;
		this.name = name;
		this.email = email;
		this.username = username;
		this.password = password;
	}*/

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

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public String getUser() {
		return username;
	}

	public void setUser(String username) {
		this.username = username;
	}

	public String getPassword() {
		return password;
	}

	public void setPassword(String password) {
		this.password = password;
	}

	public long getId() {
		return cedula;
	}

	public void setId(long cedula) {
		this.cedula = cedula;
	}

	public Set<Role> getRoles() {
		return roles;
	}

	public void setRoles(Set<Role> roles) {
		this.roles = roles;
	}
}
