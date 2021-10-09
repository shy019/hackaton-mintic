package co.com.mintic.hackaton.repository;

import java.util.Optional;

import javax.transaction.Transactional;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.stereotype.Repository;

import co.com.mintic.hackaton.models.RefreshToken;
import co.com.mintic.hackaton.models.User;


@Repository
public interface RefreshTokenRepository extends JpaRepository<RefreshToken, Long> {
  Optional<RefreshToken> findByToken(String token);
  
  Optional<RefreshToken> findByUser(User user);

  @Transactional
  @Modifying
  int deleteByUser(User user);
}
